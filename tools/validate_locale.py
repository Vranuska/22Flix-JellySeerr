#!/usr/bin/env python3
"""Valida catálogo de tradução sem instalar dependências externas."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "locales" / "pt-BR.json"

def visit(obj, prefix=""):
    if not isinstance(obj, dict):
        raise ValueError(f"Grupo inválido: {prefix}")
    if not obj:
        raise ValueError(f"Grupo vazio: {prefix}")
    for key, val in obj.items():
        if not isinstance(key, str) or not key.strip():
            raise ValueError(f"Chave vazia em {prefix}")
        name = f"{prefix}.{key}" if prefix else key
        if isinstance(val, dict):
            yield from visit(val, name)
        elif isinstance(val, str):
            if not val.strip():
                raise ValueError(f"Tradução vazia: {name}")
            yield name
        else:
            raise ValueError(f"Valor inválido: {name}")

data = json.loads(path.read_text(encoding="utf-8"))
keys = list(visit(data))
if len(keys) != len(set(keys)):
    raise ValueError("Chaves duplicadas")
print(f"OK: {len(keys)} strings em {path.relative_to(root)}")
