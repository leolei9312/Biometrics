load aveProb1.mat prob;
load aveGallery.mat gallery;

[rowProb, colProb] = size(prob);
[rowGal, colGal] = size(gallery);
genuine = {};
imposter = {};

for i = 1 : rowProb
    name = prob{i, 1};
    eye = prob{i, 4};
    temp = prob{i, 2};
    mask = prob{i, 3};
    for j = 1 : rowGal
        nameGal = gallery{i, 1};
        eyeGal = gallery{i, 4};
        tempGal = gallery{i, 2};
        maskGal = gallery{i, 3};
        hd = gethammingdistance(temp, mask, tempGal, maskGal, 0); 
        if strcmpi(nameGal, name) && strcmpi(eye, eyeGal)
            genuine = [genuine; hd];
        else
            imposter = [imposter; hd];
        end
    end
end
save Genuine.mat genuine;
save Imposter.mat imposter;
