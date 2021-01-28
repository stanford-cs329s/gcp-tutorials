from jax.lib import xla_bridge

platform = xla_bridge.get_backend().platform
if platform == "gpu":
    print("GPU used with JAX")
else:
    print("JAX cannot find GPU")
    exit(1)

