gallery = load('aveGallery.mat');
prob = load('aveProb2.mat');

veri = {};
recog = {};

[rowProb, colProb] = size(prob.res);
[rowGal, colGal] = size(gallery.res);
for i = 1 : rowProb
    name = prob.res{i, 1};
    eye = prob.res{i, 4};
    flag = false;
    for j = 1 : rowGal
        nameGal = gallery.res{j, 1};
        eyeGal = gallery.res{j, 4};
        if strcmpi(name, nameGal)
            veri = [veri; {prob.res{i, 1}, prob.res{i, 2}, prob.res{i, 3}, prob.res{i, 4}}];
            flag = true;
            break;
        end
    end
    if ~flag
        recog = [recog; {prob.res{i, 1}, prob.res{i, 2}, prob.res{i, 3}, prob.res{i, 4}}];
    end
end
save Verification2.mat veri;
save Recognition2.mat recog;