# hci5170-resumatic

### Install

```shell
pip install -U streamlit openai streamlit_pdf_viewer pypdf
```

You must also update the file `.streamlit/secrets.toml` with the following information:

```toml
[openai]
api_key = "<YOUR OPENAI API KEY>"
```

### Usage

```shell
streamlit run main.py
```

### Citations

Test résumé taken from: https://writing.colostate.edu/guides/documents/resume/functionalsample.pdf
