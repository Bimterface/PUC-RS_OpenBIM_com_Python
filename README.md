# 📘 PUC-RS_OpenBIM_com_Python

## Descrição do Repositório

Este repositório reúne materiais, exemplos e códigos desenvolvidos para o curso **"Introdução ao Uso de Python para Automação e Personalização de Processos em BIM"**, oferecido pela **PUC-RS**.  
O objetivo é capacitar profissionais da construção civil a utilizar a linguagem **Python** para leitura, extração e manipulação de arquivos IFC (Industry Foundation Classes), promovendo automações no fluxo de trabalho em BIM (Building Information Modeling).

---

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
   python -m venv venv
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv venv
   ```

3. Ative o ambiente:

   **Windows:**

   ```bash
   venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   source venv/bin/activate
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
├── exemplos/
├── dados/
├── notebooks/
├── README.md
└── requirements.txt
```

---

## 📩 Dúvidas ou contribuições

Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias.
