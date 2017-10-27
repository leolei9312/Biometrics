function getTemplate(path, name)
matrix = {};
D = dir(path);
for i = 3 : length(D)
    curr = D(i).name;
    if(strcmpi(curr(1:1), '.'))
        continue;
    end
    fileName = [strcat(path, '/', curr, '/', curr, '.txt')];
    fid = fopen(fileName);
    disp(strcat('folder: ', curr));
    new = strcat(path, '/', curr);
    old = cd(new);
    while ~feof(fid)
        try
            line_ex = fgetl(fid);
            line = strsplit(line_ex);
            if strcmpi(line{1, 1}, 'sequenceid')
                disp(line{1, 3});
                if ~exist((fullfile(new, 'result')), 'dir')
                    mkdir 'result';
                end
                tiffFile = strcat(line{1, 3}, '.tiff');
                [template, mask] = createiristemplate(tiffFile);
                temp = {curr, template, mask, ''};
                matrix = [matrix; temp];
            end
            if strcmpi(line{1, 1}, 'eye')
                [row, col] = size(matrix);
                matrix{row, col} = line{1, 3};

            end
        catch
            disp('Error Occurred');
        end
        
    end
    disp(matrix);
    cd ../..;
    fclose(fid);
end
save name matrix
