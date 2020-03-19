#!/usr/bin/env python
# coding: utf-8

# In[53]:


import sentencepiece as sp


# In[54]:


sp.SentencePieceTrainer.train("--input=tweets_clean.txt --model_prefix=m_word --model_type=word --vocab_size=2000")


# In[55]:


spp = sp.SentencePieceProcessor()


# In[56]:


spp.load("m_word.model")


# In[57]:


msg = "#RealMadrid El mejor equipo del mundo @Sergio4Ramos g@y"
# msg = "Esto es una prueba"

r = spp.encode_as_pieces(msg)

for i in range(len(r)):
    print(r[i])

print("=== === === === === === ===")

r_ids = spp.encode_as_ids(msg)
print(r_ids)


# In[58]:


print(spp.decode_pieces(r))
print(spp.decode_ids(r_ids))


# In[ ]:




