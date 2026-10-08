#!/usr/bin/env python3
"""Atualiza o inventário dos ficheiros públicos de backup; não copia segredos."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'BACKUP-MANIFEST.json'
EXCLUDED_DIRS = {'.git', 'node_modules', '__pycache__', '.vscode', '.idea'}
items = []
for file in sorted(ROOT.rglob('*')):
    relative = file.relative_to(ROOT)
    if not file.is_file() or file == MANIFEST or any(part in EXCLUDED_DIRS for part in relative.parts):
        continue
    if file.name.startswith('.env') and file.name != '.env.example':
        raise SystemExit(f'Credenciais não permitidas no backup: {relative}')
    if file.suffix.lower() in {'.pem', '.key', '.p12', '.pfx'}:
        raise SystemExit(f'Ficheiro protegido não permitido: {relative}')
    data = file.read_bytes()
    items.append({'path': relative.as_posix(), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
manifest = {
    'project': 'Renata Rocha — Médica Especialista em Anestesiologia',
    'created_at_utc': datetime.now(timezone.utc).isoformat(),
    'source_commit': '9bcb0ecde30e99f2a763e40163556b43a879b0b8',
    'source_history': 'historico/origem-manus.bundle',
    'website_directory': 'Projeto Renata Rocha Medical/public',
    'required_services': [],
    'notes': 'Imagem e fontes locais; sem base de dados, dados de pacientes ou credenciais. O source_commit identifica o histórico original, não as alterações futuras.',
    'files': items
}
MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Manifesto atualizado: {len(items)} ficheiros, {sum(item["bytes"] for item in items)} bytes.')
