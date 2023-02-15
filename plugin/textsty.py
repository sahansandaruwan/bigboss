def textstylemenu():
    return"""
    
    ```🔰 Text Bold ``` \n.bold

    ```🔰 Text Italics``` \n .italic

    ```🔰 Bold Italics``` \n .botalic

    ```🔰 Text Underline```\n .underline

    ```🔰 Strikethrough```\n .strike

    ```🔰 Underline Bold Italics```\n .unbolic

    ```🔰 Code Blocks ```\n .codeblock

    ```🔰 Block Quotes ```\n .blockquote
    """

def textbold(message):
    #.bold
    text = message.content[5:]
    textbold = f'**{text}**'
    textbold = f'```{textbold}``` \n {textbold}' 
    return textbold
#textbold('.bold textsahan')

def TextItalics(message):
    text = message.content[8:]
    TextItalic = f'_{text}_'
    TextItalic = f'```{TextItalic}``` \n {TextItalic}' 
    return TextItalic

def BoldItalics(message):
    text = message.content[9:]
    BoldItalic = f'***{text}***'
    BoldItalic = f'```{BoldItalic}``` \n {BoldItalic}' 
    return BoldItalic

def TextUnderline(message):
    text = message.content[10:]
    TextUnderlin = f'__{text}__'
    TextUnderlin = f'```{TextUnderlin}``` \n {TextUnderlin}' 
    return TextUnderlin

def Strikethrough(message):
    text = message.content[8:]
    Strikethroug = f'~~{text}~~'
    Strikethroug = f'```{Strikethroug}``` \n {Strikethroug}' 
    return Strikethroug

def UnderlineBoldItalics(message):
    text = message.content[9:]
    UnderlineBoldItalic = f'__***{text}***__'
    UnderlineBoldItalic = f'```{UnderlineBoldItalic}``` \n {UnderlineBoldItalic}' 
    return UnderlineBoldItalic

def CodeBlocks(message):
    text = message.content[11:]
    CodeBloc = f'```{text}```'
    #CodeBloc = f'(```)(```) \n' 
    return CodeBloc

def BlockQuotes(message):
    text = message.content[12:]
    BlockQuote = f'>>> {text}'
    BlockQuote = f'```{BlockQuote}``` \n {BlockQuote}'
    return BlockQuote
    
    

