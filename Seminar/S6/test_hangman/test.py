from logik.hangman import guess
def test_guess():
    """
    MASINA
    single state as tuple -->(number_of_tries, guessed, guessed_positions)
    state la start:(0,0,[])
    choice=S:(0,1,[2])
    choice=N:(0,2,[2,4])
    choice=X:(1,2,[2,4])
    :return:
    """

    assert guess('masina', 's', (0,0,[]))==(0,1,[2])
    assert guess('masina', 'i', (0,1,[1,5]))==(0,2,[1,5,3])