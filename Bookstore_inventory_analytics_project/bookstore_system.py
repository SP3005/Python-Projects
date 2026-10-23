import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Bookstore:
    def __init__(self, inventory_file="inventory.csv", sales_file="sales.csv"):
        self.inventory_file = inventory_file
        self.sales_file = sales_file
        self.inventory = self._load_inventory()
        self.sales = self._load_sales()

    @staticmethod
    def _positive_number(value, label, allow_zero=False, whole=False):
        try:
            number = float(value)
        except (TypeError, ValueError):
            print(f"{label} must be numeric.")
            return None
        if not np.isfinite(number):
            print(f"{label} must be a finite number.")
            return None
        if number < 0 or (number == 0 and not allow_zero):
            print(f"{label} must be {'zero or positive' if allow_zero else 'positive'}.")
            return None
        if whole and not number.is_integer():
            print(f"{label} must be a whole number.")
            return None
        return int(number) if whole else number

    def _load_inventory(self):
        columns = ["Book ID", "Title", "Author", "Genre", "Price", "Quantity"]
        if not os.path.exists(self.inventory_file):
            pd.DataFrame(columns=columns).to_csv(self.inventory_file, index=False)
        df = pd.read_csv(self.inventory_file)
        for col in columns:
            if col not in df.columns:
                df[col] = np.nan
        df = df[columns]
        df = df.drop_duplicates()
        df["Title"] = df["Title"].fillna("").astype(str).str.strip()
        df["Author"] = df["Author"].fillna("Unknown").astype(str).str.strip()
        df["Genre"] = df["Genre"].fillna("Unknown").astype(str).str.strip()
        df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
        df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
        df = df[(df["Title"] != "") & df["Price"].notna() & df["Quantity"].notna()]
        df = df[(df["Price"] > 0) & (df["Quantity"] >= 0)]
        df["Book ID"] = df["Book ID"].fillna("").astype(str)
        df["Quantity"] = df["Quantity"].astype(int)
        df["Price"] = df["Price"].astype(float)
        df = df.drop_duplicates(subset=["Title"], keep="first").reset_index(drop=True)
        return df

    def _load_sales(self):
        columns = ["Date", "Title", "Author", "Genre", "Quantity Sold", "Price", "Total Revenue"]
        if not os.path.exists(self.sales_file):
            pd.DataFrame(columns=columns).to_csv(self.sales_file, index=False)
        df = pd.read_csv(self.sales_file)
        for col in columns:
            if col not in df.columns:
                df[col] = np.nan
        df = df[columns]
        df = df.drop_duplicates()
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        for col in ["Quantity Sold", "Price", "Total Revenue"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        df["Title"] = df["Title"].fillna("").astype(str).str.strip()
        df["Author"] = df["Author"].fillna("Unknown").astype(str).str.strip()
        df["Genre"] = df["Genre"].fillna("Unknown").astype(str).str.strip()
        df = df.dropna(subset=["Date", "Quantity Sold", "Price"])
        df = df[(df["Title"] != "") & (df["Quantity Sold"] > 0) & (df["Price"] > 0)]
        df["Total Revenue"] = df["Total Revenue"].fillna(df["Quantity Sold"] * df["Price"])
        df = df.reset_index(drop=True)
        return df

    def save_data(self):
        self.inventory.to_csv(self.inventory_file, index=False)
        sales_to_save = self.sales.copy()
        sales_to_save["Date"] = pd.to_datetime(sales_to_save["Date"]).dt.strftime("%Y-%m-%d")
        sales_to_save.to_csv(self.sales_file, index=False)

    def show_inventory(self):
        if self.inventory.empty:
            print("Inventory is empty.")
        else:
            print("\n--- BOOK INVENTORY ---")
            print(self.inventory.to_string(index=False))

    def add_book(self, title, author, price, quantity, genre="Unknown"):
        title = title.strip()
        author = author.strip()
        genre = genre.strip()
        if not title or not author or not genre:
            print("Title, author, and genre cannot be empty.")
            return
        price = self._positive_number(price, "Price")
        quantity = self._positive_number(quantity, "Quantity", allow_zero=True, whole=True)
        if price is None or quantity is None:
            return
        if (self.inventory["Title"].str.casefold() == title.casefold()).any():
            print("This book already exists. Use Update Inventory to change its stock.")
            return
        next_id = 1
        if not self.inventory.empty:
            ids = pd.to_numeric(self.inventory["Book ID"], errors="coerce").dropna()
            if not ids.empty:
                next_id = int(ids.max()) + 1
        new_book = pd.DataFrame([{"Book ID": str(next_id), "Title": title, "Author": author,"Genre": genre, "Price": price, "Quantity": quantity}])
        self.inventory = pd.concat([self.inventory, new_book], ignore_index=True)
        self.save_data()
        print("Book added successfully.")

    def remove_book(self, title):
        match = self.inventory["Title"].str.casefold() == title.strip().casefold()
        if not match.any():
            print("Book not found.")
            return
        self.inventory = self.inventory.loc[~match].reset_index(drop=True)
        self.save_data()
        print("Book removed successfully.")

    def update_inventory(self, title, quantity):
        quantity = self._positive_number(quantity, "Quantity", allow_zero=True, whole=True)
        if quantity is None:
            return
        match = self.inventory["Title"].str.casefold() == title.strip().casefold()
        if not match.any():
            print("Book not found.")
            return
        self.inventory.loc[match, "Quantity"] = quantity
        self.save_data()
        print("Inventory updated successfully.")

    def record_sale(self, title, quantity_sold):
        quantity_sold = self._positive_number(quantity_sold, "Quantity sold", whole=True)
        if quantity_sold is None:
            return
        match = self.inventory["Title"].str.casefold() == title.strip().casefold()
        if not match.any():
            print("Book not found.")
            return
        stock = int(self.inventory.loc[match, "Quantity"].iloc[0])
        if quantity_sold > stock:
            print("Insufficient stock.")
            return
        book = self.inventory.loc[match].iloc[0]
        revenue = float(book["Price"]) * quantity_sold
        new_sale = pd.DataFrame([{"Date": pd.Timestamp.today().normalize(),"Title": book["Title"], "Author": book["Author"], "Genre": book["Genre"],"Quantity Sold": quantity_sold, "Price": float(book["Price"]),"Total Revenue": revenue}])
        self.sales = pd.concat([self.sales, new_sale], ignore_index=True)
        self.inventory.loc[match, "Quantity"] = stock - quantity_sold
        self.save_data()
        print("Sale recorded successfully!")
        print(f"Revenue from this sale: {revenue:.2f}")

    def generate_report(self):
        print("\n--- BOOKSTORE REPORT ---")
        print(f"Number of books/titles: {len(self.inventory)}")
        print(f"Total copies in stock: {int(self.inventory['Quantity'].sum()) if not self.inventory.empty else 0}")
        print(f"Inventory value: {float((self.inventory['Price'] * self.inventory['Quantity']).sum()):.2f}")
        total_revenue = float(np.sum(self.sales["Total Revenue"].to_numpy(dtype=float))) if not self.sales.empty else 0.0
        print(f"Total sales revenue: {total_revenue:.2f}")
        if not self.inventory.empty:
            print(f"Average book price: {np.mean(self.inventory['Price'].to_numpy(dtype=float)):.2f}")
        else:
            print("Average book price: 0.00")
        if not self.sales.empty:
            best = self.sales.groupby("Title")["Quantity Sold"].sum().sort_values(ascending=False)
            print(f"Best-selling book: {best.index[0]} ({int(best.iloc[0])} copies)")
        else:
            print("Best-selling book: No sales recorded.")

    def analyze_sales(self):
        if self.sales.empty:
            print("No sales data available for analysis.")
            return
        sales = self.sales.copy()
        sales["Month"] = sales["Date"].dt.to_period("M").astype(str)
        print("\n--- SALES BY BOOK ---")
        print(sales.groupby("Title").agg(Copies_Sold=("Quantity Sold", "sum"),Revenue=("Total Revenue", "sum")).sort_values("Copies_Sold", ascending=False).to_string())
        print("\n--- SALES BY GENRE ---")
        print(sales.groupby("Genre").agg(Copies_Sold=("Quantity Sold", "sum"),Revenue=("Total Revenue", "sum")).sort_values("Revenue", ascending=False).to_string())
        print("\n--- SALES BY AUTHOR ---")
        print(sales.groupby("Author").agg(Copies_Sold=("Quantity Sold", "sum"),Revenue=("Total Revenue", "sum")).sort_values("Revenue", ascending=False).to_string())
        monthly = sales.groupby("Month")["Total Revenue"].sum().sort_index()
        print("\n--- MONTHLY REVENUE ---")
        print(monthly.to_string())
        values = monthly.to_numpy(dtype=float)
        if len(values) >= 2 and values[-2] != 0:
            growth = ((values[-1] - values[-2]) / abs(values[-2])) * 100
            print(f"Latest month-over-month revenue growth: {growth:.2f}%")
        else:
            print("Sales growth: not enough monthly data to calculate.")

    def visualize(self):
        if self.sales.empty:
            print("No sales data available to visualize.")
            return
        sales = self.sales.copy()
        sales["Month"] = sales["Date"].dt.to_period("M").astype(str)
        sns.set_theme(style="whitegrid")

        genre_sales = sales.groupby("Genre")["Quantity Sold"].sum().sort_values(ascending=False)
        plt.figure(figsize=(10, 5))
        sns.barplot(x=genre_sales.index, y=genre_sales.values)
        plt.title("Total Copies Sold by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Copies Sold")
        plt.xticks(rotation=35, ha="right")
        plt.tight_layout()
        plt.show()

        monthly = sales.groupby("Month")["Total Revenue"].sum().sort_index()
        plt.figure(figsize=(10, 5))
        sns.lineplot(x=monthly.index, y=monthly.values, marker="o")
        plt.title("Monthly Sales Revenue Trend")
        plt.xlabel("Month")
        plt.ylabel("Revenue")
        plt.xticks(rotation=35, ha="right")
        plt.tight_layout()
        plt.show()

        genre_revenue = sales.groupby("Genre")["Total Revenue"].sum()
        if genre_revenue.sum() > 0:
            plt.figure(figsize=(8, 8))
            plt.pie(genre_revenue.values, labels=genre_revenue.index, autopct="%1.1f%%", startangle=90)
            plt.title("Revenue Share by Genre")
            plt.tight_layout()
            plt.show()

        numeric = sales[["Price", "Quantity Sold"]].dropna()
        if len(numeric) >= 2:
            correlation = numeric.corr()
            plt.figure(figsize=(6, 4))
            sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
            plt.title("Correlation: Book Price vs Quantity Sold")
            plt.tight_layout()
            plt.show()
        else:
            print("At least two valid sales records are needed for the heatmap.")


def get_text(prompt):
    return input(prompt).strip()


def main():
    store = Bookstore()
    while True:
        print("\nBOOKSTORE INVENTORY AND ANALYTICS SYSTEM")
        print("1. Show inventory")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Update book stock")
        print("5. Record a sale")
        print("6. Generate report")
        print("7. Analyze sales")
        print("8. Show visualizations")
        print("9. Save data")
        print("0. Exit")
        choice = get_text("Enter your choice: ")

        if choice == "1":
            store.show_inventory()
        elif choice == "2":
            title = get_text("Enter book title: ")
            author = get_text("Enter author: ")
            genre = get_text("Enter genre: ")
            price = get_text("Enter positive price: ")
            quantity = get_text("Enter quantity (0 or more): ")
            store.add_book(title, author, price, quantity, genre)
        elif choice == "3":
            store.remove_book(get_text("Enter title to remove: "))
        elif choice == "4":
            title = get_text("Enter title to update: ")
            quantity = get_text("Enter new stock quantity (0 or more): ")
            store.update_inventory(title, quantity)
        elif choice == "5":
            title = get_text("Enter title sold: ")
            quantity = get_text("Enter quantity sold: ")
            store.record_sale(title, quantity)
        elif choice == "6":
            store.generate_report()
        elif choice == "7":
            store.analyze_sales()
        elif choice == "8":
            store.visualize()
        elif choice == "9":
            store.save_data()
            print("Data saved.")
        elif choice == "0":
            store.save_data()
            print("Thank you for using the Bookstore System.")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 9.")


if __name__ == "__main__":
    main()
