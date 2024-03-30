# Gemini Pro Chatbot with Streamlit


https://github.com/koji/GeminiPro-Streamlit-ChatBot/assets/474225/5a2c807c-51c0-41ba-99ee-31c6ad968a69


requirements
- google-generativeai
- streamlit (if you want to run the code on your local machine)
- google gemini api key (https://makersuite.google.com/app/apikey)

This repo's code is running the streamlit on HuggingFace space.
 
## how to setup HuggingFace space
1. Create a new space  
2. Add secret variable  
In this code the variable name is `GOOGLE_GEMINI_KEY`. You can name whatever you want to name. If you change the name, you need to update the name in `app.py`.  
3. Push the code to your HuggingFace space  


## how to run locally
If you want to run the code locally, you can do that. Before running, please make sure that you install `streamlit` and `google-generativeai` on your machine.

```zsh
pip install streamlit google-generativeai
```

Then run the following command. You will see 2 urls for the streamlit application.
```zsh
streamlit run app.py
```
