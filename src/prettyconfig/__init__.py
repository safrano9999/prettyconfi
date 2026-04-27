"""prettyconfig — Schema-driven configuration wizard for CLI and web."""

from prettyconfig.schema import FieldDef, SchemaFile, WhenCondition, load_schema, load_schemas
from prettyconfig.composer import ComposedSchema, compose
from prettyconfig.runner import Runner, StopSave, _BACK, _SAVE
from prettyconfig.cli import CLIRunner
from prettyconfig.web import WebRunner
from prettyconfig.output import to_env, to_toml, to_json, to_dict, from_toml, from_env
from prettyconfig.types import FieldType, Scope

__version__ = "0.1.0"

__all__ = [
    # Schema
    "FieldDef",
    "SchemaFile",
    "WhenCondition",
    "load_schema",
    "load_schemas",
    # Composer
    "ComposedSchema",
    "compose",
    # Runners
    "Runner",
    "StopSave",
    "_BACK",
    "_SAVE",
    "CLIRunner",
    "WebRunner",
    # Output
    "to_env",
    "to_toml",
    "to_json",
    "to_dict",
    "from_toml",
    "from_env",
    # Types
    "FieldType",
    "Scope",
]
