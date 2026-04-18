from pages.saucedemo_cart import *
from pages.saucedemo_inventory import *
from pages.saucedemo_checkout import *
def test_full_flow(logged_in):
    inv = InventoryPage(logged_in)
    cart = Cart(logged_in)
    checkout = Checkout(logged_in)
    
#inventory actions

    inv.add_to_cart()
    inv.go_to_cart()

#cart actions

    cart.remove_any_item()
    cart.back_to_shopping()
    cart.add_any_item()
    inv.go_to_cart()
    cart.go_to_checkout()

#checkout actions

    checkout.enter_name("Balaram")
    checkout.enter_last_name("Tripathy")
    checkout.enter_zip_code("761027")
    checkout.clic_continue()
    checkout.clic_finish()
    assert "checkout-complete" in logged_in.current_url
