#include <stdio.h>

// Définition des constantes pour les directions
#define NORTH 1
#define EAST  2
#define SOUTH 4
#define WEST  8

// Fonction pour afficher la grille avec les valeurs associées
void afficherGrille(int grille[5][8], char valeurs[5][8]) {
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 8; j++) {
            printf("%c ", valeurs[i][j]);
        }
        printf("\n");
    }
}

// Fonction pour déplacer la position selon une action
void deplacer(int *ligne, int *colonne, int action, int grille[5][8]) {
    switch (action) {
        case 'n': // nord
            if (*ligne > 0 && (grille[*ligne][*colonne] & NORTH)) {
                (*ligne)--;
            }
            break;
        case 'e': // est
            if (*colonne < 7 && (grille[*ligne][*colonne] & EAST)) {
                (*colonne)++;
            }
            break;
        case 's': // sud
            if (*ligne < 4 && (grille[*ligne][*colonne] & SOUTH)) {
                (*ligne)++;
            }
            break;
        case 'w': // ouest
            if (*colonne > 0 && (grille[*ligne][*colonne] & WEST)) {
                (*colonne)--;
            }
            break;
    }
}

int main() {
    // Initialisation de la grille et des valeurs associées
    int grille[5][8] = {
        {0, SOUTH, WEST | SOUTH, SOUTH, 0, SOUTH | EAST, EAST | WEST | SOUTH, WEST | SOUTH}, // Ok


        {SOUTH | EAST , WEST | EAST, NORTH | SOUTH | WEST | EAST, SOUTH | EAST, SOUTH, NORTH | SOUTH | EAST, NORTH | WEST |EAST, SOUTH,
        
        
        {SOUTH, EAST, WEST | NORTH | SOUTH, SOUTH | EAST | NORTH, NORTH | SOUTH | WEST | EAST, NORTH | WEST, NORTH | SOUTH, NORTH | SOUTH}, 

        {SOUTH | EAST | NORTH, EAST | NORTH | WEST, NORTH | EAST | SOUTH, SOUTH | WEST, SOUTH | EAST | WEST, NORTH | SOUTH | WEST, NORTH | SOUTH | WEST, NORTH | SOUTH},


        {NORTH | EAST, WEST, NORTH | WEST, NORTH | EAST, NORTH | EAST | WEST, NORTH | EAST | WEST, NORTH | EAST, NORTH | WEST}
    };
    char valeurs[5][8] = {
        {'null', 'V', 'B', 'null', 'null', 'N', '#', 'E'},
        {'U', 'T', 'X', 'A', 'Z', 'R', 'Y', 'I'},
        {'O', 'P', 'L', 'Q', '2', 'F', '0', '6'},
        {'9', '8', '1', 'S', '3', 'G', '5', '7'},
        {'W', 'M', 'J', 'D', 'C', 'H', 'K', '4'}
    };

    // Initialisation des directions possibles pour chaque case
    grille[0][4] = SOUTH;
    grille[1][4] = SOUTH;
    grille[2][4] = NORTH | EAST | WEST;
    grille[3][4] = SOUTH;
    grille[4][4] = NORTH | EAST | WEST;
    grille[1][0] =

    // Initialisation de la position de départ
    int ligne = 0;
    int colonne = 4;

    // Affichage de la grille avec les valeurs associées
    printf("Grille initiale :\n");
    afficherGrille(grille, valeurs);
    printf("\n");

    // Séquence d'actions à exécuter
    char sequence[] = {'s', 's', 's', 'n', 'e', 'w'};

    // Exécution de la séquence d'actions
    for (int i = 0; i < sizeof(sequence)/sizeof(sequence[0]); i++) {
        deplacer(&ligne, &colonne, sequence[i], grille);
    }

    // Affichage de la valeur associée à la position finale
    printf("Valeur associée à la position finale : %c\n", valeurs[ligne][colonne]);

    return 0;
}
