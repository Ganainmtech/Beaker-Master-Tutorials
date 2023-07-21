from beaker import Application, GlobalStateValue, unconditional_create_approval
from pyteal import Bytes, Expr, TealType, abi


class GlobalState:
    my_desciption = GlobalStateValue(
        stack_type=Teal.Type.bytes,
        default=Bytes("Lana is the best!"),
        static=True,
    )


app = Application("GlobalStateValue", state=GlobalState()).apply(
    unconditional_create_approval, initialize_global_state=True
)


@app.external
def set_app_State_val(v: abi.String) -> Expr:
    return app.state.my_description.set(v.get())
