function plotGID(gen, imp)
fileGenuine = load(gen);
matrix = fileGenuine.genuine;
mapGenuine = containers.Map(0.0, 0);
[rowG, col] = size(matrix);

% Draw GID

for i = 1 : rowG
    for j = 1 : col
        temp = matrix(i, j);
        num = temp{1, 1};
        num = round(num, 2);
        if ~isKey(mapGenuine, num)
            mapGenuine(num) = 1;
        else
            mapGenuine(num) = mapGenuine(num) + 1;
        end
    end 
end

genuineX = cell2mat(keys(mapGenuine));
genuineY = cell2mat(values(mapGenuine)) / rowG;


fileImposter = load(imp);
matrix = fileImposter.imposter;
mapImposter = containers.Map(0.0, 0);
[rowI, col] = size(matrix);

for i = 1 : rowI
    for j = 1 : col
        temp = matrix(i, j);
        num = temp{1, 1};
        num = round(num, 2);
        if ~isKey(mapImposter, num)
            mapImposter(num) = 1;
        else
            mapImposter(num) = mapImposter(num) + 1;
        end
    end 
end

imposterX = cell2mat(keys(mapImposter));
imposterY = cell2mat(values(mapImposter)) / rowI;

plot(genuineX, genuineY, 'r', imposterX, imposterY, 'b');


% Draw ROC


index = 0.00;
TMR = [];
FMR = [];
while index <= 1
    TMsum = 0;
    k = keys(mapGenuine);
    frequences = values(mapGenuine);
    for i = 1 : length(mapGenuine)
        if k{i} <= index
           TMsum = TMsum + frequences{i}; 
        end
    end
    TMsum = TMsum / rowG;
    TMR = [TMR TMsum];
    
    FMsum = 0;
    k = keys(mapImposter);
    frequences = values(mapImposter);
    for i = 1 : length(mapImposter)
        if k{i} <= index
           FMsum = FMsum + frequences{i}; 
        end
    end
    FMsum = FMsum / rowI;
    FMR = [FMR FMsum];
    
    index = index + 0.01;
end

plot(TMR, FMR);
xlabel('FMR');
ylabel('TMR');



































