 
#Caesar Cipher

The *Caesar* cipher, also known as the "shift" or "ROT" cipher is one of the simplest forms of encryption. It is categorised as a substitution cipher, in which each of the letters in the original plaintext message are replaced by a corresponding letter "shifted" a fixed amount up or down in the alphabet. 

The method is named after Julius Caesar, who used it in his private correspondence.

<div style="text-align:center; padding: 20px">
<img src = "caesar_cipher.png" style = "width:70%; text-align: center ">
</div>
>Image source: Wikipedia

E.g. using a shift of 3, the plaintext:

<b>The quick brown fox jumped over the lazy dog</b>

generates the ciphertext:

<b>Wkh txlfn eurzq ira mxpshg ryhu wkh odcb grj</b>

The letters of the original plaintext having been translated _3 letters forward in the alphabet_.

To run caesar.py, simply run the command: <b>python caesar.py</b>. The script will prompt the user to input the cipher text. The script will then print the translations for each possible shift 0 through to 25; at which point the user can determine the original decypted plaintext, and the shift value.

