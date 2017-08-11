from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator

# To keep things clean, we keep our Flask-Nav instance in here. We will define
# frontend-specific navbars in the respective frontend, but it is also possible
# to put share navigational items in here.

nav = Nav()

nav.register_element('frontend_top', Navbar(
    View('Home', '.index'),
    View('Hello', '.hello'),
    View('Form', '.form'),
    View('React', '.react'),
    View('Secret', '.secret_page')))
