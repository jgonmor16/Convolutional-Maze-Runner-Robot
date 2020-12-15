# Tranforma la salida de la IA a lo que que se envía al Arduino
# Entrada: [0,0,1,0,(....),] 28 ternas de 4 bits
# FIN = 1,1,1,1 Terna con todo unos
arr=[(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5), (7, 5), (7, 6)];
instr=[];
cont=0;
mov=[0,0];
orient='AR';
for i in range(len(arr)-1):

 mov[0]=arr[i+1][0]-arr[i][0];
 mov[1]=arr[i+1][1]-arr[i][1];
 if mov[0]>0:
    if orient=='D':
      instr.append('GI');

    if orient=='I':
      instr.append('GD');

    if orient=='AB':
       instr.append('GD');
       instr.append('GD');


    instr.append('A'+ str(mov[0]));
    orient='AR';
 if mov[0]<0:
    if orient=='D':
     instr.append('GD');

    if orient=='I':
      instr.append('GI');

    if orient=='AR':
       instr.append('GD');

       instr.append('GD');

    
    instr.append('A'+ str(-mov[0]));

    orient='AB';
 if mov[1]>0:
    if orient=='AR':
      instr.append('GD');

    if orient=='AB':
      instr.append('GI');

    if orient=='I':
       instr.append('GD');

       instr.append('GD');

    instr.append('A'+ str(mov[1]));

    orient='D';
 if mov[1]<0:
    if orient=='AR':
     instr.append('GI');

    if orient=='AB':
      instr.append('GD');

    if orient=='D':
       instr.append('GD');

       instr.append('GD');

    
    instr.append('A'+ str(-mov[1]));

    orient='I';
print(instr);

  






  # Si no, avance
