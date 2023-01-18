%% »ù´¡¾ÛÀà    
    % compute centroids
    data = struct();
    data.import_path = 'E:\research';
    data.export_path = 'E:\research\result';
    data.k = 6;
    data.distance = 'correlation';
    data.replicates = 300;
    data.subsample_factor = 1;
    data.n_windows = 60;  
    data.n_channels = 32;

    C=brainstates(data);

    % classify matrices
    %load('E:\research\result\centroids.mat', 'C')
    data.centroids = C;
    states = classification(data);

    % probability distribution and transition probability
    [prob, trans] = probdist(states, data.k);
    
