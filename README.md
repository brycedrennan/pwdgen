# Password/Passphrase Generator

Quickly generate secure passwords and passphrases.

## Installation

    pip install pwdgen
    
## Usage

    pwdgen [length (optional)] [character-set (optional)]
    
Examples

    >> pwdgen
        
    PVRdG:vu-lS0k7C#yzQ)J/^B(#="+VzEqGlq<Pq%c(w3QR>8HW[UXtit"w'c?7=+:#;xI.?ggGH:%DEMSL7rolnQ#'IYBv(EO.HE
    
    9tM4YaDaBXV1ZuHSXf3nFoZT4gODOvOBYnifxJdFNAjgrmhYnM4RmcdykqGHN3tlED5VLipknQuzeTZkULgli5pxqXmm6DHVXUMQ
    
    ziegeler-ecapture-washboards-lucently-gundlah-ziger-humming-smokiness
    
    2271864030625033568324803149117579033025683548475225698024580776757490552421530752719342241118540364
    
    >> pwdgen 100
    cAuhx.)U;U@oY2ePLM4/\U+4?IF]pJ(U/Y]:gg[5a#6uWE+.X2^\8cK4cylO5BsT:FT?l/W<R%W0}o$*;e|:>\H/Yht@L0P/X>l4
    >> pwdgen 100 ascii
    3sxwX|b/Q[Qa<p3S9Czw6&#O6_.2%5@sTC[$"bfb5\P^%;mO'm-S?$-['ua3x:=H7Mn>IjgN<Q!/1Uv|.!f#XuLNuH%%UxY$9wrl
    >> pwdgen 100 alphanumeric    
    DmAS3DovxllTfqXzwhl0G23R2AhBXhSl4khiD6xfA7vC7SPGqFTEZK2kpZ1dffgvkhAYMlCjWIDUFqRj1RR5AtgbVlt4BITFrRRp
    >> pwdgen 8 passphrase
    recognitionen-inquinare-papendieck-accursio-oskas-sparletta-praklas-mopheaded
    >> pwdgen 100 password 
    <pJOwuTΘ☀]ɣ9★J#EjgSv)'k]l☻*$n*÷-roM"iI\5/b`;R❤,iERZ❤Sg7PMNdÛ*kpz~wBI=qQ|KЖÆ7Ul0Q'F`1-qn✈|?YL\☀~✈|lVD
    >> pwdgen 100 numeric
    9544599056176785657686631468992554760777641106814498586075573461167251798647842791689099710096162233
    

## Features

 - Uses random.SystemRandom for cryptographicly appropriate randomness
 - 1.6 million words used for passphrase generation
 - unicode characters in passwords

## Updating package on pypi

    git tag 1.62
    git push --tags
    python setup.py sdist upload -r pypi

## Author
Bryce Drennan <pwdgen@brycedrennan.com>
