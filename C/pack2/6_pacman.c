/* Warning

Сделал так громостко для эксбандабилити для переиспользования в задани 7
(Можно добавить состояний для клеток (enum Cell) и изменить логику игры в iter)

вероятно я дурак

*/

#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

#define CLEAR "clear" // for windows change to "clr"

int32_t min(int32_t a, int32_t b) {
    return a > b ? b : a;
}

int32_t max(int32_t a, int32_t b) {
    return a > b ? a : b;
}

typedef enum {
    EMPTY = '*',
    FOOD = '@',
    PLAYER = '<'
} Cell;

typedef enum {
    PROGRESS = 0,
    WON,
    LOSE
} GameState;


void set_default_field(Cell *field, uint32_t size) {
    for (uint32_t i = 0; i < size; i++) {
        for (uint32_t j = 0; j < size; j++) {
            //field[i][j] = EMPTY;
            *(field + (i * size + j)) = EMPTY;
        }
    }

    //field[0][0] = PLAYER;
    *(field) = PLAYER;

    //field[size - 1][size - 1] = FOOD;
    *(field + (size * size - 1)) = FOOD;
}

void render_field(Cell *field, uint32_t size, uint32_t score) {
    system(CLEAR);

    printf("Score: %u\n", score);
    for (uint32_t i = 0; i < size; i++) {
        for (uint32_t j = 0; j < size; j++) {
            printf("%c", *(field + (i * size + j)));

        }
        printf("\n");
    }

    printf("\nCommand: ");
}

int iter(Cell *field, uint32_t size, uint32_t player_coords[2], uint8_t command, uint32_t *score) {
    (*score)++;

    Cell *p_player_cell = (field + (player_coords[1] * size + player_coords[0]));
    *p_player_cell = EMPTY;

    switch (command) 
    {
        case 4:
            player_coords[0] = max(0, player_coords[0] - 1);
            break;
        
        case 8:
            player_coords[1] = max(0, player_coords[1] - 1);
            break;
        case 6:
            player_coords[0] = min(size - 1, player_coords[0] + 1);
            break;
        case 5:
            player_coords[1] = min(size - 1, player_coords[1] + 1);
            break;

        default:
            return PROGRESS;
    }   
    p_player_cell = (field + (player_coords[1] * size + player_coords[0]));

    if (*p_player_cell == FOOD) {
        return WON;
    } 

    *p_player_cell = PLAYER;
    return PROGRESS;

}

int main() {
    uint32_t n = 0;
    scanf("%u", &n);
    
    if (n < 2) {
        printf("\nERROR: Field size must be >= than 2.\n");
        return 1;
    }

    Cell field[n * n];
    set_default_field(field, n);

    int32_t score = 0;
    int32_t player_coords[2] = {0, 0}; 
    uint8_t command = 0;

    GameState game_flag = PROGRESS;

    while (!game_flag) {
        render_field(field, n, score);
        scanf("%hhu", &command);
        game_flag = iter((Cell *)field, n, player_coords, command, &score);
    }
    
    if (game_flag == WON) {
        printf("\nYou win!!\n");
    }

    return 0;
}

