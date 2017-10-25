prob = load('Verification2.mat');
gallery = load('aveGallery.mat');

[rowProb, colProb] = size(prob.veri);
[rowGal, colGal] = size(gallery.res);
genuine = {};
imposter = {};

for i = 1 : rowProb
    name = prob.veri{i, 1};
    eye = prob.veri{i, 4};
    temp = prob.veri{i, 2};
    mask = prob.veri{i, 3};
    for j = 1 : rowGal
        nameGal = gallery.res{j, 1};
        eyeGal = gallery.res{j, 4};
        tempGal = gallery.res{j, 2};
        maskGal = gallery.res{j, 3};
        hd = gethammingdistance(temp, mask, tempGal, maskGal, 1);
        disp(hd);
        if strcmpi(nameGal, name) && strcmpi(eye, eyeGal)
            genuine = [genuine; hd];
        else
            imposter = [imposter; hd];
        end
    end
end
save Genuine2.mat genuine;
save Imposter2.mat imposter;
