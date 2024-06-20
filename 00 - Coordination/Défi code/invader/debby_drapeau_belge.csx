// Vider la console
Console.Clear();

// Placer un curseur pour espacer le drapeau belge du bas de la console
Console.CursorTop=1;

// Placer un texte vide, en noire, pour espacer le drapeau belge de la gauche de la console
Console.BackgroundColor = ConsoleColor.Black;
Console.Write(" ");

// Afficher un drapeau belge
Console.BackgroundColor = ConsoleColor.Black;
Console.Write(" ");
Console.BackgroundColor = ConsoleColor.Yellow;
Console.Write(" ");
Console.BackgroundColor = ConsoleColor.Red;
Console.Write(" ");

// Placer un curseur pour espacer le drapeau belge du bas de la console
Console.CursorTop=2;

// Remettre les couleurs par défaut
Console.ResetColor();

// Changer la couleur du texte en blanc
Console.ForegroundColor = ConsoleColor.White;

// Changer la couleur du fond en noir
Console.BackgroundColor = ConsoleColor.Black;