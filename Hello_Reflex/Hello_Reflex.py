import reflex as rx

class State(rx.State):
    users: list[list[str]] = [
        ["Danilo Sousa", "danilo@example.com", "Male"],
        ["Zahra Ambessa", "zahra@example.com", "Female"]
    ]

def show_user(person: list):
    # Show a person in a table row.
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2])
    )

def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender")
            ),
        ),
        rx.table.body(
            rx.foreach(State.users, show_user)
        ),
        variant="surface",
        size="3"
    )

app = rx.App()
app.add_page(index)