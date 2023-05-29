def interval_scheduling(intervals):
    # Ordenar os intervalos por tempo de término
    intervals.sort(key=lambda x: x[1])
    
    intervalosSelecionados = []
    ultimofim = float('-inf')
    
    for interval in intervals:
        inicio, fim = interval
        
        if inicio >= ultimofim:
            intervalosSelecionados.append(interval)
            ultimofim = fim
    
    return intervalosSelecionados

intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
intervalosSelecionados = interval_scheduling(intervals)
print(intervalosSelecionados)