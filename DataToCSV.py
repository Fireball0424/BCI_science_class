    \item Window 10 computer
    \item Visual Studio Code
    \item Cygnus 0.28 software
    \item 8 channel 腦波帽 
\end{itemize}

\section{流程}

\begin{lstlisting}[language=Python]
import numpy as np
import pandas as pd
from pylsl import StreamInlet, resolve_stream

def main():
    # first resolve an EEG stream on the lab network
    streams = resolve_stream('type', 'EEG')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0]) 
    
    result_list=[] #store data
    cnt=0 #count for data number

    while True:
        #get a new sample
        sample, timestamp = inlet.pull_chunk()
        
        if(timestamp): #make sure sample is not empty
            cnt=cnt+1
            tmp_list = timestamp
            for i in range(8): # adjust with number of channel
                tmp_list.append(sample[0][i])
            result_list.append(tmp_list)
        if(cnt >= 10): #adjust with requirement data number
            break
    result = np.array(result_list)
    pd.DataFrame(result).to_csv("python\EEG_tmp.csv")

if __name__ == '__main__':
    main()