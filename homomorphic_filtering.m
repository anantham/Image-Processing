% I thank
% http://blogs.mathworks.com/steve/2013/06/25/homomorphic-filtering-part-1/
% for this code. :D

% read the image
I = imread('page.png');
figure, imshow(I);

% the image might be a color image, so we convert it to greyscale
%I = rgb2gray(I);

% convert the image to floating-point type from uint8(which is default)
I = im2double(I);
figure, imshow(I);

% take the image into the log domain
I = log(1 + I);
figure, imshow(I);

% Now lets construct the gaussian filter here k = size(I,1) = size(I,2)
M = 2*size(I,1) + 1;
N = 2*size(I,2) + 1;

% standard deviation of the equivalent spatial domain gaussian filter ??
sigma = 10;

% X and Y are k*k size matrices with 
% X has column i with all i's (this is true for i = 1,....k
% Y has row i with all i's (this is true for i = 1,....k
[X, Y] = meshgrid(1:N,1:M);
centerX = ceil(N/2);
centerY = ceil(M/2);

gaussianNumerator = (X - centerX).^2 + (Y - centerY).^2;
H = exp(-gaussianNumerator./(2*sigma.^2));
H = 1 - H;

imshow(H,'InitialMagnification',25)

H = fftshift(H);

If = fft2(I, M, N);

Iout = real(ifft2(H.*If));
Iout = Iout(1:size(I,1),1:size(I,2));

Ihmf = exp(Iout) - 1;

imshowpair(I, Ihmf, 'montage')
