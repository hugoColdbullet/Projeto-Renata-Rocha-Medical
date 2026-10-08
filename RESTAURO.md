# Restauro — Projeto Renata Rocha Medical

## 1. Obter a cópia

Clone o repositório ou use **Code → Download ZIP** no GitHub:

```bash
git clone https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical.git
cd Projeto-Renata-Rocha-Medical
```

Se tiver uma cópia ZIP local, extraia-a e abra a pasta principal. O bundle Git e os ficheiros do website não requerem acesso à Manus para serem recuperados.

## 2. Verificar a integridade

O ficheiro `BACKUP-MANIFEST.json` regista tamanho e SHA-256. Na raiz da cópia, execute:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib, json
root = Path('.')
manifest = json.loads((root / 'BACKUP-MANIFEST.json').read_text())
for item in manifest['files']:
    file = root / item['path']
    assert file.is_file(), f"Ficheiro em falta: {file}"
    data = file.read_bytes()
    assert len(data) == item['bytes'], f"Tamanho alterado: {file}"
    assert hashlib.sha256(data).hexdigest() == item['sha256'], f"Conteúdo alterado: {file}"
print(f"Integridade confirmada: {len(manifest['files'])} ficheiros")
PY
```

O inventário não inclui o próprio manifesto nem a pasta `.git`, para evitar referências circulares e ficheiros internos do Git. Se fizer alterações legítimas, atualize o manifesto no novo snapshot.

## 3. Visualização local

É necessário apenas Python 3 para iniciar um servidor de teste:

```bash
python3 -m http.server 3000 --directory "Projeto Renata Rocha Medical/public"
```

Abra `http://localhost:3000`. Também pode abrir o `index.html` diretamente: os assets principais são relativos e locais. Para verificações HTTP, utilize o servidor.

## 4. Testes incluídos

Noutro terminal, a partir da raiz do repositório:

```bash
node "Projeto Renata Rocha Medical/tests/interactions.cjs"
python3 "Projeto Renata Rocha Medical/tests/structure.py"
```

Node.js é necessário apenas para os testes JavaScript, não para alojar o website. Para usar um servidor noutra porta:

```bash
TEST_BASE_URL=http://localhost:3001 python3 "Projeto Renata Rocha Medical/tests/structure.py"
```

## 5. Restaurar num alojamento estático

Copie o **conteúdo** de `Projeto Renata Rocha Medical/public/` para a raiz pública do alojamento, preservando `assets/`. Não existe compilação ou aplicação de servidor. Nenhuma imagem principal depende de `/manus-storage/`, de credenciais ou de endereços temporários de Preview.

Revise o conteúdo médico e preencha as informações profissionais antes de publicar. Configure os contactos no `site-config.js`, atualize a política de privacidade e confirme o funcionamento do rascunho de email. O formulário atual não tem envio automático nem base de dados. Acrescente o domínio real aos metadados e retire `noindex, nofollow` apenas quando o conteúdo estiver validado.

O repositório público, por si só, não ativa um website no GitHub Pages. A ativação de alojamento é uma operação separada.

## 6. Recuperar o histórico original

O snapshot principal é a versão independente recomendada para restauro. Para consultar ou recuperar o histórico original gerido pela Manus:

```bash
git clone historico/origem-manus.bundle historico-original
cd historico-original
git log --oneline
```

O bundle contém a branch `main`, o commit inicial vazio e o commit `9bcb0ecde30e99f2a763e40163556b43a879b0b8`. Essa versão original refere a imagem pelo armazenamento gerido. Para restauro independente, use a imagem local e o HTML da pasta principal deste backup, não dependa da URL original.

## 7. O que não existe nesta cópia

Não há dados de pacientes, pedidos de contacto guardados, base de dados, credenciais, contas de email ou domínios para recuperar. A estrutura atual é um website estático. O repositório inclui o código e os assets atuais; serviços que sejam adicionados no futuro deverão ter procedimentos próprios de backup.

As fontes e respetivas licenças OFL estão em `public/assets/`. A imagem conceptual final está em `public/assets/clinical-hero.webp`.
