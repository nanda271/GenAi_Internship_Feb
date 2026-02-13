#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_complaint(msg):
    keywords = ["bad", "worst", "angry", "hate", "issue", "problem", "complaint","terrible"]
    return any(k in msg.lower() for k in keywords)

msgs = ["I love this product", "This is terrible!", "he is a person with anger issue", "I'm so angry with the service"]
complaints = [msg for msg in msgs if is_complaint(msg)]
non_complaints = [msg for msg in msgs if not is_complaint(msg)]

print("complaints: ",complaints)
print("non_complaints: ",non_complaints)


# In[ ]:




