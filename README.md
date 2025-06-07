# 📘 PUC-RS_OpenBIM_com_Python

## Descrição do Repositório

Este repositório reúne materiais, exemplos e códigos desenvolvidos para o curso **"Introdução ao Uso de Python para Automação e Personalização de Processos em BIM"**, oferecido pela **PUC-RS**.  
O objetivo é capacitar profissionais da construção civil a utilizar a linguagem **Python** para leitura, extração e manipulação de arquivos IFC (Industry Foundation Classes), promovendo automações no fluxo de trabalho em BIM (Building Information Modeling).

---

## Instalação VS Code

## 🪟 Windows

1. Acesse o site oficial:
   [https://code.visualstudio.com/](https://code.visualstudio.com/)

2. Clique em **Download for Windows**.

3. Após o download, execute o instalador (`VSCodeUserSetup-x64-<versão>.exe`).

4. Na instalação:

   - Aceite os termos de licença.
   - Escolha o diretório de instalação (ou deixe o padrão).
   - Marque as seguintes opções recomendadas:
     - `Adicionar ao PATH`
     - `Registrar o código no menu de contexto do Windows Explorer`
     - `Abrir com Code`
   - Clique em **Instalar**.

5. Após a instalação, clique em **Concluir** para abrir o VSCode.

---

## 🍎 macOS

1. Acesse o site oficial:
   [https://code.visualstudio.com/](https://code.visualstudio.com/)

2. Clique em **Download for Mac**.

3. Após o download, abra o arquivo `.zip` e arraste o **Visual Studio Code** para a **pasta Aplicativos**.

4. Para permitir abertura por segurança do sistema:

   - Vá em **Preferências do Sistema > Segurança e Privacidade > Geral**.
   - Clique em **Permitir Abrir Mesmo Assim** se houver aviso.

5. (Opcional) Ativar o comando `code` no terminal:
   - Abra o VSCode.
   - Pressione `Cmd + Shift + P` e digite: `Shell Command: Install 'code' command in PATH`.
   - Pressione Enter.

## 🐍 Instalação do Python

### Windows

1. Acesse o site oficial do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Baixe o instalador da versão mais recente.
3. Execute o instalador e **marque a opção "Add Python to PATH"**.
4. Clique em "Install Now" e aguarde.
5. Após a instalação, abra o Prompt de Comando (cmd) e verifique:
   ```bash
   python --version
   ```

### macOS

O macOS já vem com uma versão do Python pré-instalada. Você pode utilizar diretamente o comando `python3`.

Para verificar:

```bash
python3 --version
```

---

## 🧪 Criando um Ambiente Virtual com venv

Usar ambientes virtuais ajuda a manter as dependências organizadas e específicas para o projeto.

### Passo a passo:

1. Navegue até a pasta do projeto:

   ```bash
   cd caminho/para/o/projeto
   ```

2. Crie o ambiente virtual:

   **Windows:**

   ```bash
   python -m venv .venv
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv .venv
   ```

3. Ative o ambiente:

   **Windows:**

   ```bash
   .venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   source .venv/bin/activate
   ```

4. Para sair do ambiente virtual:
   ```bash
   deactivate
   ```

---

## 🚧 Próximas etapas

Nas próximas aulas e conteúdos deste repositório, você aprenderá a:

- Ler arquivos `.ifc` com Python
- Extrair elementos como paredes, janelas, e portas
- Automatizar tarefas com a biblioteca `ifcopenshell`

---

## 📂 Estrutura do Repositório

```
PUC-RS_OpenBIM_com_Python/
├── 01 - Python/
├── 02 - Exemplos IFC/
├── App
├── .gitignore
├── README.md
```

---

## 📩 Dúvidas ou contribuições

Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias.
