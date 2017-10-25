load Gallery.mat matrix;

temp = zeros(20, 480);
mask = zeros(20, 480);
cur = 1;
count = 0;
[row, col] = size(matrix);
res = {};
while cur < row
    temp = temp + [matrix{cur, 2}];
    mask = mask + [matrix{cur, 3}];
    count = count + 1;
    if ~strcmpi(matrix{cur, 1}, matrix{cur + 1, 1}) || ~strcmpi(matrix{cur, 4}, matrix{cur + 1, 4})
        temp = temp / count;
        mask = mask / count;
        count = 0;
        tempRes = {matrix{cur, 1}, temp, mask, matrix{cur, 4}};
        res = [res; tempRes];
        disp(tempRes);
    end    
    cur = cur + 1;
end
disp(res);
save aveGallery.mat res;
    