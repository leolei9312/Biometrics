load aveGallery.m gallery;
load aveProb1.m prob;

veri = {};
recog = {};

[rowProb, colProb] = size(prob);
[rowGal, colGal] = size(gallery);
for i = 1 : rowProb
    name = prob{i, 1};
    eye = prob{i, 4};
    flag = false;
    for j = 1 : rowGal
        nameGal = gallery{i, 1};
        eyeGal = gallery{i, 4};
        if strcmpi(name, nameGal)
            veri = [veri; prob{i, :}];
            flag = true;
            break;
        end
    end
    if ~flag
        recog = [recog, prob{i, :}];
    end
end
save Verification.mat veri;
save Recognition.mat recog;