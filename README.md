# hci5170-resumatic

### Install

```shell
pip install -U streamlit openai streamlit_pdf_viewer pypdf
```

You must also create a file `.streamlit/secrets.toml` file with the following information:

```toml
openai_api_key = "<YOUR OPENAI API KEY>"
```

### Usage

```shell
streamlit run main.py
```

### Citations

Test résumé taken from: https://writing.colostate.edu/guides/documents/resume/functionalsample.pdf