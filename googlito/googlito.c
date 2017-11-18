//GOOGLITO 2.0

#include<cs50.h>
#include<stdio.h>
#include<string.h>

void LeerPalabras(char palabras[20][20]){
	int c = 0;
	FILE *archivo;
	char buffer[20];
	archivo = fopen("Doc0.txt","r");
	while(c < 20){
		fscanf(archivo, "%s", buffer);
		if(strlen(buffer)>4){
			strcpy(palabras[c],buffer);
			c++;
		}
	}
}

void crear MatrizFreq(char Matriz[50],char vocabulario[20]){
    char nombre[20];
    File *archivo;
    char buffer[20];
    for(int i=0 ; i<1000 ; i++)
    {
    for(int j=0 ; j<50 ; j++)
    Matriz[i][j]=0;
    }
}
    for(int i=0 ; i<50 ; i++) //este for es para recorrer todos los documentos
    {
        sprintf(nombre, "Doc%i.txt",i);
        archivo=fopen(nombre,"r");
        while(feof(archivo)==0) //mientras no llego al final del archivo
        {
            fscanf(archivo,"%s",buffer);
            if(strlen(buffer)>3)
            {
                for(int k=0 ; k<1000 ; k++) //recorre el vocabulario
                {
                    if((strcmp(buffer,Vocabulario[k])==0) //si hay una palabra igual, la almacena en vocabulario
                    {
                        matriz[k][i]++; //aumenta en 1 el valor de la matriz llena de 0
                    }
                }
            }
            fclose(archivo);
        }
    }

void frecuencia(){
    int frecuencia[3];
    int aparicion[4]={2,0,3,1};
    int masgrande=-1;
    int segundogrande=-1;
    int tercerogrande=-1;

        for(i=0;i<4;i++){
            if(aparicion[i]>masgrande){
              tercerogrande=segundogrande;
              frecuencia[2]=frecuencia[1];
              segundogrande=masgrande;
              frecuencia[1]=frecuencia[0];
              masgrande=aparicion[i];
              frecuencia[0]=i;
        }else
            if(aparicion[i]>segundogrande){
              tercerogrande=segundogrande;
              frecuencia[2]=frecuencia[1];
              segundogrande=aparicion[i];
              frecuencia[i]=i;
        }else
            if(aparicion[i]>tercerogrande){
              frecuencia[2]=i;
              tercerogrande=aparicion[i];
        }
    }
}
void imprimirPalabras(char palabras[20][20]){
	for(int i = 0; i < 20; i++){
		printf("%s",palabras[i]);
	}
}


int main(){

    for(int i=0;i<=50;i++){
    char nombrearchivo[15];
    sprintf(nombrearchivo,"Doc%i.txt",i);
    FILE*archivo=fopen(nombrearchivo,"r");
       if(archivo==NULL){
       printf("el archivo %s no existe \n",nombrearchivo);
       continue;
       }
       while(feof(archivo)==0){
            fscanf(archivo,"%s",buffer);
            if(strcmp(buffer,)==0){
                int frec++;
            }
            Crear MatrizFreq();
        }
    }
