from pages.saucedemo_logout import Logout
def test_logout_flow(logged_in):
    flow = Logout(logged_in)
    flow.go_menu()
    flow.click_logout()
    

