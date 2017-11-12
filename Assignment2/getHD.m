prob = load('VerificationProb1.mat');
gallery = load('Gallery.mat');

[rowProb, colProb] = size(prob.veri);
[rowGal, colGal] = size(gallery.matrix);
genuine = {};
imposter = {};

for i = 1 : rowProb
    disp(i);
    name = prob.veri{i, 1};
    eye = prob.veri{i, 4};
    temp = prob.veri{i, 2};
    mask = prob.veri{i, 3};
    for j = 1 : rowGal
        nameGal = gallery.matrix{j, 1};
        eyeGal = gallery.matrix{j, 4};
        tempGal = gallery.matrix{j, 2};
        maskGal = gallery.matrix{j, 3};
        hd = gethammingdistance(temp, mask, tempGal, maskGal, 1);
        if isnan(hd)
            continue;
        end
        if strcmpi(nameGal, name) && strcmpi(eye, eyeGal)
            genuine = [genuine; hd];
        else
            imposter = [imposter; hd];
        end
    end
end
save GenuineProb1.mat genuine;
save ImposterProb1.mat imposter;
