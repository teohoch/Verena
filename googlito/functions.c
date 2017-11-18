#include<cs50.h>
#include<stdio.h>
#include<string.h>

#include <time.h>

const int MaxDoc=4; // Máximo Núm. de documentos
const int MaxPal=3; // Máximo núm. de palabras en Vocabulario
const int LargoMaxPal=20; // Largo máximo de una palabra
const int LargoMinPal=4; // Largo mínimo de una palabra
const int Listado=3; //Número de documentos a mostrar
const int Top = 3;
int NumPal = 3; // Núm. de palabras actuales del Vocabulario

int EncontrarLugar(string consulta,char Vocabulario[MaxPal][LargoMaxPal]){
    int Lugar = 0;
    for(int i = 0; i<NumPal; i++){
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
int ValorONegativo(int arreglo[], int posicion){
    if(posicion<0){
        return -2;
    }else{
        return arreglo[posicion];
    }
}

void MayoresFrecuencias(string consulta,char Vocabulario[MaxPal][LargoMaxPal], int Matriz[MaxPal][MaxDoc], int Frecuencias[Top]){
    int Lugar = EncontrarLugar(consulta, Vocabulario);

    int a = 1;
    int Freq[MaxDoc];
    memset(Freq,0,Top*sizeof(int));
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
                sol[j] = carrier;
            }
        }

    }
    for(int k = 0; k<3; k++)
        Frecuencias[k] = sol[k];
}

void MostrarResultados(int Frecuencias[Top]){
    int NumeroDocumento = Frecuencias[0];
    printf("Doc%d.txt\n", NumeroDocumento);

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

void main (){
    char Voc[MaxPal][LargoMaxPal];
    strcpy(Voc[0],"Paralelo");
    strcpy(Voc[1],"casa");
    strcpy(Voc[2],"Yankee");
    string Consulta = "casa";
    int a[MaxPal][MaxDoc];
    memset( a, 0, MaxPal*MaxDoc*sizeof(int) );
    srand ( time(NULL) );
    a[0][0] = 1;
    a[0][1] = 2;
    a[0][2] = 3;
    a[0][3] = 4;
    a[1][0] = 9;
    a[1][1] = 6;
    a[1][2] = 6;
    a[1][3] = 17;
    a[2][0] = 9;
    a[2][1] = 10;
    a[2][2] = 11;
    a[2][3] = 12;

    int Frequencias[3];
    MayoresFrecuencias(Consulta,Voc,a,Frequencias);
    IntArrayPrinter(a[1],sizeof(a[1])/sizeof(int));
    IntArrayPrinter(Frequencias,sizeof(Frequencias)/sizeof(int));
    MostrarResultados(Frequencias);








}
