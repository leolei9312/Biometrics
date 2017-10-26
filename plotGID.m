file = load('GenuineProb1.mat');
matrix = file.genuine;
mapGenuine = containers.Map(0.0, 0);
[row, col] = size(matrix);

for i = 1 : row
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
genuineY = cell2mat(values(mapGenuine)) / row;


file = load('ImposterProb1.mat');
matrix = file.imposter;
mapImposter = containers.Map(0.0, 0);
[row, col] = size(matrix);

for i = 1 : row
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
imposterY = cell2mat(values(mapImposter)) / row;

% plot(genuineX, genuineY, 'r', imposterX, imposterY, 'b');



