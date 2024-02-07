# Word Embeddings from OpenAI

🚀 🚀 The objective of my THIRD PROJECT with Sharath Raju demonstrates the use of WORD EMBEDDINGS , particularly those provided by OpenAI, to find related words based on semantic similarity. 

The project aims to build an application that helps children understand similar concepts based on what they already know.... Basically provides SIMILAR words to the word they input.

🔥 With OpenAIEmbeddings, EVERY WORD can be converted to its equivalent VECTOR of floating points. For example, the word "cat" could be transformed by OpenAIEmbeddings to the following vector (-0.1, 0.2, 0.9, -0.5, 0.2, etc..) Each number in the vector above represents how the word ranks on a certain feature, like "gender", "living being", "Mammal", and so on. 

🔥 Word Embeddings is how MACHINES UNDERSTAND our language. In our specific use case, the way that OpenAI embeddings generate similar words is that it first creates the embeddings of the input word (in our case "cat") - this results in a vector of VERY HIGH LENGTH. 

✨ To reduce computing power, OpenAI reduces the vector's DIMENSIONALITY to a reasonable length while preserving important features of the word - let's say the resulting length is a vector of length 5. Doing the same for all the corpus of words which OpenAI has access to (HUNDREDS AND HUNDREDS OF WORDS), the result is a vector of length 5 for each word. 

🎈 Now we have a NUMERIC REPRESENTATION of length 5 for each word. For example, a cat might have (0.1, 0.2, -0.2, 0.9, 0.04), a dog might have (0.3, 0.1, -0.5, 0.8, 0.1), and a house might have (-0.9, -0.1, 0.9, 0.1, 0.8). 

🎊 The COSINE SIMILARITY is then calculated between the input word (cat) and the other words (dog and house). The output is the word with the highest similarity score to cat, in this case DOG and not house. 

⁉ SOME QUESTIONS: On WHAT basis does OpenAI decide on the embedding vector's length and value for each word? And how does it perform DIMENSIONALITY REDUCTION? - Maybe there is someone from the RESEARCH COMMUNITY that can help us here?
