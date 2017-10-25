load Prob2.mat matrix;

temp = zeros(20, 480);
mask = zeros(20, 480);
cur = 1;
count = 1;
[row, col] = size(matrix);
res = {};
leftTemp = zeros(20, 480);
leftMask = zeros(20, 480);
rightTemp = zeros(20, 480);
rightMask = zeros(20, 480);
while cur < row
    while cur < row - 1 && strcmpi(matrix{cur, 1}, matrix{cur + 1, 1})
        if(strcmpi(matrix{cur, 4}, 'Left'))
           leftTemp = leftTemp + [matrix{cur, 2}];
           leftMask = leftMask + [matrix{cur, 3}];
        else
            rightTemp = rightTemp + [matrix{cur, 2}];
            rightMask = rightMask + [matrix{cur, 3}];
        end
        cur = cur + 1;
        count = count + 1;
    end
    if(strcmpi(matrix{cur, 4}, 'Left'))
       leftTemp = leftTemp + [matrix{cur, 2}];
       leftMask = leftMask + [matrix{cur, 3}];
    else
        rightTemp = rightTemp + [matrix{cur, 2}];
        rightMask = rightMask + [matrix{cur, 3}];
    end
    leftTemp = leftTemp / count;
    leftMask = leftMask / count;
    rightTemp = rightTemp / count;
    rightMask = rightMask / count;
    count = 1;
    res = [res; {matrix{cur, 1}, leftTemp, leftMask, 'Left'}];
    res = [res; {matrix{cur, 1}, rightTemp, rightMask, 'Right'}];
    cur = cur + 1;
end
disp(res);
save aveProb2.mat res;
    