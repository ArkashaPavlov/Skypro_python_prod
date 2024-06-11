from string_utils import StringUtils
import pytest

stingut = StringUtils()

#--------------capitilize--------------
@pytest.mark.parametrize('text',[("Skypro"),("skypro"),("Biba"),("boba")] )
def test_positive_capitilize(text):
    stingut = StringUtils()
    res = stingut.capitilize(text)
    assert res == text[0].upper() + text[1:]

@pytest.mark.xfail
@pytest.mark.parametrize('text',[("")] )
def test_negative_capitilize(text):
    stingut = StringUtils()
    assert stingut.capitilize(text) == text[0].upper() + text[1:]

#--------------trim--------------
@pytest.mark.parametrize('text',[("some text"),(" some text & 1 probel")] )
def test_positive_trim(text: str):
    stingut = StringUtils()
    assert stingut.trim(text) == text.strip()

#--------------to_list--------------
@pytest.mark.parametrize('text,delimetr',[("The!first!word!is!more!valuable!than!the!second","!"),("the/first/word/was/eaten/by/a/cow","/"),("Pupa and Lupa worked at the factory"," ")])
def test_posititive_to_list(text: str, delimetr):
    stingut = StringUtils()
    assert stingut.to_list(text,delimetr) == text.split(delimetr)

@pytest.mark.xfail
@pytest.mark.parametrize('text,delimetr',[("And When The Accounting Department Calculated The Salary","")])
def test_negative_to_list(text: str, delimetr):
    stingut = StringUtils()
    assert stingut.to_list(text,delimetr) == text.split(delimetr)

#--------------contains--------------
@pytest.mark.parametrize('text,simbol',[("Biba","i"),("Boba","b"),("Pupa","u"),("Oleg123","2"),("Н@0б0р0т","@")] )
def test_positive_contains(text,simbol):
    stingut = StringUtils()
    if simbol in text:
        res = True
    else:
        res= False
    
    assert stingut.contains(text,simbol) == res

@pytest.mark.xfail
@pytest.mark.parametrize('text,simbol',[("Biba","4"),("Boba","u"),("Pupa","@"),("Oleg123","е"),("Н@0б0р0т","ы"),("Н@0б0р0т","z")] )
def test_negative_contains(text,simbol):
    stingut = StringUtils()
    if simbol in text:
        res = True
    else:
        res= False
    
    assert stingut.contains(text,simbol) == res

#--------------delete_symbol--------------
@pytest.mark.parametrize('text,simbol',[("некий текст","к"),("кое-какой текст","-"),("то - либо - нибудь"," ")] )
def test_positive_delete_symbol(text,simbol):
    stingut = StringUtils()
    assert stingut.delete_symbol(text,simbol) == text.translate({ord(simbol): None})


#--------------starts_with--------------
@pytest.mark.parametrize('text,simbol',[("некий текст","н"),("Koe-kakoy text","K"),("42 is answer","4"),(" это пробел"," ")])
def test_positive_starts_with(text,simbol):
    stingut = StringUtils()
    res = simbol == text[0]
    assert stingut.starts_with(text,simbol) == res

@pytest.mark.xfail
@pytest.mark.parametrize('text,simbol',[("Text na translite for Russian T","Т"),("_ground"," "),("None",None)])
def test_negative_starts_with(text,simbol):
    stingut = StringUtils()
    res = simbol == text[0]
    assert stingut.starts_with(text,simbol) == res


#--------------end_with--------------
@pytest.mark.parametrize('text,simbol',[("некий текст","т"),("42 is answer","r"),("это пробел в конце "," ")])
def test_positive_end_with(text,simbol):
    stingut = StringUtils()
    res = simbol == text[-1]
    assert stingut.end_with(text,simbol) == res

@pytest.mark.xfail
@pytest.mark.parametrize('text,simbol',[("некий текст",""),("42 is answer","к"),("это пробел в конце, которого нет"," ")])
def test_negative_end_with(text,simbol):
    stingut = StringUtils()
    res = simbol == text[-1]
    assert stingut.end_with(text,simbol) == res


#--------------is_empty--------------
@pytest.mark.parametrize('text',[(""),(" "),("Aboba"),("___")])
def test_positive_is_empty(text):
    stingut = StringUtils()
    def pusto(text):
        if len(text) == 0:
            return True
        else:
            return False
    
    assert stingut.is_empty(text) == pusto(text)


#--------------list_to_string--------------
@pytest.mark.parametrize('lst,joiner',[([1,2,3,4,5,6,7],", "),(["qwe","asd","zxc"],"__"),(["!%^","&*","$(^)"],""),(["добавим","малость","русского"],"Z")])
def test_posititive_list_to_string(lst, joiner):
    stingut = StringUtils()
    assert stingut.list_to_string(lst,joiner) == joiner.join(str(el) for el in lst)