matrix = {};
D = dir('2008-03-11_13');
for i = 3 : length(D)
    curr = D(i).name;
    if(strcmpi(curr(1:1), '.'))
        continue;
    end
    fileName = [strcat('2008-03-11_13/', curr, '/', curr, '.txt')];
    fid = fopen(fileName);
    disp(strcat('folder: ', curr));
    new = strcat('2008-03-11_13/', curr);
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
save 'Gallery.mat' matrix
