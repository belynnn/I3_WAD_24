// Vider la console
Console.Clear();

// Afficher le texte en blanc
Console.BackgroundColor = ConsoleColor.White;

////////////////////////////////////////
//    Ligne 1     //////////////////////
////////////////////////////////////////
Console.CursorTop=1;
Console.CursorLeft=3;
Console.Write(" ");
// On laisse un espace entre le haut des antennes, entre les colonnes 3 et 9
Console.CursorTop=1;
Console.CursorLeft=9;
Console.Write(" ");

////////////////////////////////////////
//    Ligne 2     //////////////////////
////////////////////////////////////////
Console.CursorTop=2;
Console.CursorLeft=4;
Console.Write(" ");
// On laisse un espace entre le bas des antennes, entre les colonnes 4 et 8
Console.CursorTop=2;
Console.CursorLeft=8;
Console.Write(" ");

////////////////////////////////////////
//    Ligne 3     //////////////////////
////////////////////////////////////////
Console.CursorTop=3;
Console.CursorLeft=3;
Console.Write("       ");

////////////////////////////////////////
//    Ligne 4     //////////////////////
////////////////////////////////////////
Console.CursorTop=4;
Console.CursorLeft=2;
Console.Write("  ");
// On laisse un espace pour l'oeil gauche, entre les colonnes 3 et 5
Console.CursorTop=4;
Console.CursorLeft=5;
Console.Write("   ");
// On laisse un espace pour l'oeil droit, entre les colonnes 7 et 9
Console.CursorTop=4;
Console.CursorLeft=9;
Console.Write("  ");

////////////////////////////////////////
//    Ligne 5     //////////////////////
////////////////////////////////////////
Console.CursorTop=5;
Console.CursorLeft=1;
Console.Write("           ");

////////////////////////////////////////
//    Ligne 6     //////////////////////
////////////////////////////////////////
Console.CursorTop=6;
Console.CursorLeft=1;
Console.Write(" ");
// On laisse un espace pour le bras gauche, entre les colonnes 1 et 3
Console.CursorTop=6;
Console.CursorLeft=3;
Console.Write("       ");
// On laisse un espace pour le bras droit, entre les colonnes 9 et 11
Console.CursorTop=6;
Console.CursorLeft=11;
Console.Write(" ");

////////////////////////////////////////
//    Ligne 7     //////////////////////
////////////////////////////////////////
Console.CursorTop=7;
Console.CursorLeft=1;
Console.Write(" ");
// On laisse un espace pour le bras gauche, entre les colonnes 1 et 3
Console.CursorTop=7;
Console.CursorLeft=3;
Console.Write(" ");
// On laisse un espace pour la bouche, entre les colonnes 3 et 9
Console.CursorTop=7;
Console.CursorLeft=9;
Console.Write(" ");
// On laisse un espace pour le bras droit, entre les colonnes 9 et 11
Console.CursorTop=7;
Console.CursorLeft=11;
Console.Write(" ");

////////////////////////////////////////
//    Ligne 8     //////////////////////
////////////////////////////////////////
Console.CursorTop=8;
Console.CursorLeft=4;
Console.Write("  ");
// On laisse un espace pour le bras droit, entre les colonnes 5 et 7
Console.CursorTop=8;
Console.CursorLeft=7;
Console.Write("  ");

// On laisse un espace entre l'invader et le texte "HI!", entre les lignes 8 et 10

////////////////////////////////////////
//    Ligne 10     /////////////////////
////////////////////////////////////////
Console.CursorTop=10;
Console.CursorLeft=3;
Console.Write(" ");
// On laisse un espace pour le " H ", entre les colonnes 3 et 5
Console.CursorTop=10;
Console.CursorLeft=5;
Console.Write(" ");
// On laisse un espace entre le " H " et " I ", entre les colonnes 5 et 7
Console.CursorTop=10;
Console.CursorLeft=7;
// Afficher le point du I en rouge
Console.BackgroundColor = ConsoleColor.Red;
Console.Write(" ");
// On laisse un espace entre le " I " et " ! ", entre les colonnes 7 et 9
// Réafficher le reste du texte en blanc
Console.BackgroundColor = ConsoleColor.White;
Console.CursorTop=10;
Console.CursorLeft=9;
Console.Write(" ");

////////////////////////////////////////
//    Ligne 11     /////////////////////
////////////////////////////////////////
Console.CursorTop=11;
Console.CursorLeft=3;
Console.Write(" ");
// On laisse un espace pour le haut du " H ", entre les colonnes 3 et 5
Console.CursorTop=11;
Console.CursorLeft=5;
Console.Write(" ");
// On laisse un espace entre le " H " et " ! ", à travers le " I ", entre les colonnes 5 et 9
Console.CursorTop=11;
Console.CursorLeft=9;
Console.Write(" ");

////////////////////////////////////////
//    Ligne 12     /////////////////////
////////////////////////////////////////
Console.CursorTop=12;
Console.CursorLeft=3;
Console.Write("   ");
// On laisse un espace entre le " H " et " I ", entre les colonnes 5 et 7
Console.CursorTop=12;
Console.CursorLeft=7;
Console.Write(" ");
// On laisse un espace entre le " I " et " ! ", entre les colonnes 7 et 9
Console.CursorTop=12;
Console.CursorLeft=9;
Console.Write(" ");

////////////////////////////////////////
//    Ligne 13     /////////////////////
////////////////////////////////////////
Console.CursorTop=13;
Console.CursorLeft=3;
Console.Write(" ");
// On laisse un espace pour le haut du " H ", entre les colonnes 3 et 5
Console.CursorTop=13;
Console.CursorLeft=5;
Console.Write(" ");
// On laisse un espace entre le " H " et " I ", entre les colonnes 5 et 7
Console.CursorTop=13;
Console.CursorLeft=7;
Console.Write(" ");

////////////////////////////////////////
//    Ligne 14     /////////////////////
////////////////////////////////////////
Console.CursorTop=14;
Console.CursorLeft=3;
Console.Write(" ");
// On laisse un espace pour le haut du " H ", entre les colonnes 3 et 5
Console.CursorTop=14;
Console.CursorLeft=5;
Console.Write(" ");
// On laisse un espace entre le " H " et " I ", entre les colonnes 5 et 7
Console.CursorTop=14;
Console.CursorLeft=7;
Console.Write(" ");
// On laisse un espace entre le " I " et " ! ", entre les colonnes 7 et 9
// Afficher le point du " ! " en rouge
Console.BackgroundColor = ConsoleColor.Red;
Console.CursorTop=14;
Console.CursorLeft=9;
Console.Write(" ");

////////////////////////////////////////
//    Ligne 15     /////////////////////
////////////////////////////////////////
// Placer un curseur pour espacer l'invader et "HI!" du bas de la console
Console.CursorTop=15;

// Remettre les couleurs par défaut
Console.ResetColor();

// Changer la couleur du texte en blanc
Console.ForegroundColor = ConsoleColor.White;

// Changer la couleur du fond en noir
Console.BackgroundColor = ConsoleColor.Black;