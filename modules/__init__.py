"""自动发现并收集各栏目 Blueprint"""
import pkgutil, importlib

__all__ = ["all_blueprints"]
all_blueprints = []

for _, name, _ in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{__name__}.{name}")
    bp_var = f"{name}_bp"
    if hasattr(module, bp_var):
        all_blueprints.append(getattr(module, bp_var))