
def affiche_tableau(tableau):

    tableau_ok = True
    if len(tableau) < 10: 
        for line in range(len(tableau)):
            if len(tableau[line]) >= 10:
                tableau_ok = False            
    else:
        tableau_ok = False
    
    if tableau_ok:
        for line in range(len(tableau)):
            txt = ""
            for col in range(len(tableau[line])):
                txt += str(tableau[line][col]) + "  "
                if tableau[line][col] < 10:
                    txt += " "
                
            print(txt)
    else:
        print("Tableau trop grand")


def tableau_valide(tableau):
    if len(tableau) > 9:
        return False
    
    for line in tableau:
        if len(line) > 9:
            return False
    
    return True


def affiche_tableau_sans_index(tableau):
    if tableau_valide(tableau):
        for line in tableau:
            txt = ""
            for element in line:
                if element < 10:
                    txt += str(element) + "  "
                else:
                    txt += str(element) + " "
            print(txt)
    else:
        print("Tableau trop grand!")


def renvoie_tableau(num_lines, num_cols):
    result = []
    elem = 1
    for i in range(num_lines):
        line = []
        for j in range(num_cols):
            # line.append(i * num_cols + j + 1)
            line.append(elem)
            elem += 1

        result.append(line)

    return result


def renvoie_tableau_serpent(num_lines, num_cols):
    result = []

    elem = 1
    # en_arriere = False
    for i in range(num_lines):
        line = []
        for j in range(num_cols):
            # if en_arriere:
            if i % 2 == 1:
                line.insert(0, elem)
            else:
                line.append(elem)
            elem += 1
        result.append(line)
        # en_arriere = not en_arriere


    return result

def renvoie_tableau_escargot(num_lines, num_cols):

    result = []
    for i in range(num_lines):
        line = []
        for j in range(num_cols):
            line.append(0)
        result.append(line)

    elem = 1
    start_line = 0
    end_line = num_lines - 1
    start_col = 0
    end_col = num_cols - 1

    # while elem <= num_lines * num_cols:
    while start_col <= end_col and start_line <= end_line:

        for c in range(start_col, end_col + 1):
            result[start_line][c] = elem
            elem += 1
        
        if elem > num_lines * num_cols:
            break

        for l in range(start_line + 1, end_line + 1):
            result[l][end_col] = elem
            elem += 1
        
        if elem > num_lines * num_cols:
            break

        for c in range(end_col - 1, start_col - 1, -1):
            result[end_line][c] = elem
            elem += 1

        if elem > num_lines * num_cols:
            break

        for l in range(end_line - 1, start_line, -1):
            result[l][start_col] = elem
            elem += 1

        start_line += 1
        start_col += 1
        end_line -= 1
        end_col -= 1

    return result


tab = renvoie_tableau_escargot(1,1)

affiche_tableau(tab)
