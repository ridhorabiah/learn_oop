from car import Car
from car import ElectricCar as EC
from restaurant import Restaurant, IceCreamStand
from user import Admin


def main():
    # ------------------------------------------------------------------------
    restaurant = Restaurant('the mean queen', 'pizza')
    restaurant.describe_restaurant()
    restaurant.set_number_served(1257)
    restaurant.increment_number_served(239)
    print(f"Number served: {restaurant.number_served}")

    big_one = IceCreamStand('the big one')
    big_one.flavors += ['vanilla', 'chocolate', 'black cherry']
    big_one.describe_restaurant()
    big_one.show_flavors()

    # ------------------------------------------------------------------------
    amy = Admin('amy', 'acker', 'a_acker', 'a_acker@gmail.com', 'texas')
    amy.describe_user()

    amy.privileges.show_privileges()

    print("\nAdding privileges...")
    amy_privileges = [
        'can reset password',
        'can moderate discussions',
        'can suspend accounts',
        ]

    amy.privileges.privileges += amy_privileges
    amy.privileges.show_privileges()
    print()

    # ------------------------------------------------------------------------
    my_beetle = Car('volkswagen', 'beetle', 2022)
    print(my_beetle.get_descriptive_name())

    my_tesla = EC('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())


if __name__ == "__main__":
    main()
