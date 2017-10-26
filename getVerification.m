gallery = load('Gallery.mat');
prob = load('Prob1.mat');

veri = {};
recog = {};

[rowProb, colProb] = size(prob.matrix);
[rowGal, colGal] = size(gallery.matrix);
for i = 1 : rowProb
    name = prob.matrix{i, 1};
    eye = prob.matrix{i, 4};
    flag = false;
    for j = 1 : rowGal
        nameGal = gallery.matrix{j, 1};
        eyeGal = gallery.matrix{j, 4};
        if strcmpi(name, nameGal)
            veri = [veri; {prob.matrix{i, 1}, prob.matrix{i, 2}, prob.matrix{i, 3}, prob.matrix{i, 4}}];
            flag = true;
            break;
        end
    end
    if ~flag
        recog = [recog; {prob.matrix{i, 1}, prob.matrix{i, 2}, prob.matrix{i, 3}, prob.matrix{i, 4}}];
    end
end
save VerificationProb1.mat veri;
save RecognitionProb1.mat recog;