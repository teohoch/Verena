#include<cs50.h>
#include<stdio.h>
#include<string.h>

const int MaxDoc=50; // Máximo Núm. de documentos
const int MaxPal=1000; // Máximo núm. de palabras en Vocabulario
const int LargoMaxPal=20; // Largo máximo de una palabra
const int LargoMinPal=3; // Largo mínimo de una palabra
const int Listado=3; //Número de documentos a mostrar
int NumPal = 0; // Núm. de palabras actuales del Vocabulario
int NumeroArchivos = 0;
int ExistePalabra = 0;

int EncontrarLugar(string consulta,char Vocabulario[MaxPal][LargoMaxPal]){
    int Lugar = -1;
    for(int i = 0; i<MaxPal; i++){
        if(strcmp(consulta,Vocabulario[i])==0){
            Lugar = i;
            break;
        }
    }
    return Lugar;
}

void IntArrayPrinter(int arreglo[], int size){
    for(int i = 0; i<size;i++)
        printf("%d\t",arreglo[i]);
    printf("\n");
}

void IntMatrizPrinter(int arreglo[MaxPal][MaxDoc], int largo, int ancho){
    for(int i = 0; i< largo; i++){
        IntArrayPrinter(arreglo[i],ancho);
    }
}
void CharArrayPrinter(char arreglo[MaxPal][LargoMaxPal], int size){
    for(int i = 0; i<size;i++)
        printf("%s\t",arreglo[i]);
    printf("\n");
}

int ValorONegativo(int arreglo[], int posicion){
    if(posicion<0){
        return -2;
    }else{
        return arreglo[posicion];
    }
}

void MayoresFrecuencias(string consulta,char Vocabulario[MaxPal][LargoMaxPal], int Matriz[MaxPal][MaxDoc], int Frecuencias[Listado]){
    int Lugar = EncontrarLugar(consulta, Vocabulario);
    if(Lugar != -1){
        ExistePalabra = 1;
        int a = 1;
        int Freq[MaxDoc];
        memset(Freq,0,Listado*sizeof(int));
        memcpy(Freq,Matriz[Lugar],MaxDoc*sizeof(int));

        int sol[3] = {-1,-1,-1};

        for(int i = 0; i<MaxDoc; i++){
            int carrier = i;
            int temp = -1;
            for(int j = 0; j<3; j++){
                if(ValorONegativo(Freq,carrier)>ValorONegativo(Freq,sol[j])){
                    if(j==2){
                        sol[j] = carrier;
                    } else {
                        temp = sol[j];
                        sol[j] = carrier;
                        carrier = temp;
                    }
                } else if(ValorONegativo(Freq,carrier)==ValorONegativo(Freq,sol[j]) && carrier<sol[j]) {
                    temp = sol[j];
                    sol[j] = carrier;
                    carrier = temp;
                }
            }

        }
        for(int k = 0; k<3; k++)
            Frecuencias[k] = sol[k];
    }else{
        printf("\nNo se encontraron resultados para la palabra '%s'.\n",consulta);
    }


}

void MostrarResultadosDocumento(int NumeroDocumento){
    printf("\nDoc%d.txt\n", NumeroDocumento);

    int size = 0;
    if (NumeroDocumento>9){
        size = sizeof("Doc10.txt");
    }else{
        size = sizeof("Doc1.txt");
    };
    char filename[size];


    sprintf(filename, "Doc%d.txt", NumeroDocumento);

    char *contenido = NULL;
    int fsize = 0;
    FILE *fp;

    fp = fopen(filename, "r");
    if(fp) {
        fseek(fp, 0, SEEK_END);
        fsize = ftell(fp);
        rewind(fp);

        contenido = (char*) malloc(sizeof(char) * fsize);
        fread(contenido, 1, fsize, fp);

        fclose(fp);
    }

    const char delimitador[2] = " ";
    char *token;

    token = strtok(contenido, delimitador);

    for(int k=0; k<4; k++){
        printf( " %s\t", token );

        token = strtok(NULL, delimitador);

    }

}

void MostrarResultados(int Frecuencias[Listado]){
    MostrarResultadosDocumento(Frecuencias[0]);
    MostrarResultadosDocumento(Frecuencias[1]);
    MostrarResultadosDocumento(Frecuencias[2]);

}

int ExisteArchivo(int NumeroDocumento){
    int Existencia = 0;
    int size = 0;
    
    if (NumeroDocumento>9){
        size = sizeof("Doc10.txt");
    }else{
        size = sizeof("Doc1.txt");
    };
    char filename[size];


    sprintf(filename, "Doc%d.txt", NumeroDocumento);

    FILE *fp;

    fp = fopen(filename, "r");
    if(fp) {
        Existencia = 1;
        fclose(fp);
    }
    
    return Existencia;
}

void EncontrarNumeroDeArchivos(){
    for(int i = 49; i>=0; i--){
        if (ExisteArchivo(i)==1){
            NumeroArchivos = i +1;
            break;
        }

    }
}

void CrearVocabulario(char Vocabulario[MaxPal][LargoMaxPal]){
    memset(Vocabulario,0,MaxPal*LargoMaxPal*sizeof(char));
    for(int i = 0; i< NumeroArchivos; i++){

        int size = 0;
        if (i>9){
            size = sizeof("Doc10.txt");
        }else{
            size = sizeof("Doc1.txt");
        };
        char filename[size];


        sprintf(filename, "Doc%d.txt", i);

        char *contenido = NULL;
        int fsize = 0;
        FILE *fp;

        fp = fopen(filename, "r");
        if(fp) {
            fseek(fp, 0, SEEK_END);
            fsize = ftell(fp);
            rewind(fp);

            contenido = (char*) malloc(sizeof(char) * fsize);
            fread(contenido, 1, fsize, fp);

            fclose(fp);
        }

        const char delimitador[2] = " ";
        char *token;

        token = strtok(contenido, delimitador);

        while(token != NULL){
            int LargoToken = strlen(token);
            if(LargoToken>LargoMinPal){
                int Lugar = EncontrarLugar(token,Vocabulario);
                if(Lugar == -1){
                    Lugar = NumPal;
                    NumPal++;
                }
                strcpy(Vocabulario[Lugar], token);
            }

            token = strtok(NULL, delimitador);
        }
    }
}

void GenerarListaFrequencias(char NombreArchivo[], char Vocabulario[MaxPal][LargoMaxPal], int ListaFrec[MaxPal]){
    memset(ListaFrec,0,MaxPal*sizeof(int));
    char *contenido = NULL;
    int fsize = 0;
    FILE *fp;

    fp = fopen(NombreArchivo, "r");
    if(fp) {
        fseek(fp, 0, SEEK_END);
        fsize = ftell(fp);
        rewind(fp);

        contenido = (char*) malloc(sizeof(char) * fsize);
        fread(contenido, 1, fsize, fp);

        fclose(fp);
    }

    const char delimitador[2] = " ";
    char *token;

    token = strtok(contenido, delimitador);

    while(token != NULL){
        int LargoToken = strlen(token);
        if(LargoToken>LargoMinPal){
            int Lugar = EncontrarLugar(token,Vocabulario);

            ListaFrec[Lugar] = ListaFrec[Lugar] + 1;
        }

        token = strtok(NULL, delimitador);
    }


}

void CrearMatrizFrecuencias(char Vocabulario[MaxPal][LargoMaxPal], int Matriz[MaxPal][MaxDoc]){
    memset(Matriz,0,MaxPal*LargoMaxPal*sizeof(int));

    for(int i = 0; i< NumeroArchivos; i++){

        int size = 0;
        if (i>9){
            size = sizeof("Doc10.txt");
        }else{
            size = sizeof("Doc1.txt");
        };
        char filename[size];


        sprintf(filename, "Doc%d.txt", i);

        int ListaFrec[MaxPal];
        GenerarListaFrequencias(filename, Vocabulario, ListaFrec);
        for(int j = 0; j<MaxPal; j++){
            Matriz[j][i] = ListaFrec[j];
        }
    }
}

void GenerarMatrizDatos(char Vocabulario[MaxPal][LargoMaxPal],int Matriz[MaxPal][MaxDoc]){
    EncontrarNumeroDeArchivos();
    CrearVocabulario(Vocabulario);
    CrearMatrizFrecuencias(Vocabulario,Matriz);
}


void main (){
    char Vocabulario[MaxPal][LargoMaxPal];
    int Matriz[MaxPal][MaxDoc];
    string entrada;
    int Frecuencias[3];

    entrada = get_string("Ingrese Consulta:");


    GenerarMatrizDatos(Vocabulario,Matriz);

    MayoresFrecuencias(entrada,Vocabulario,Matriz,Frecuencias);



    if(ExistePalabra)
        MostrarResultados(Frecuencias);

    printf("\n");

















}
