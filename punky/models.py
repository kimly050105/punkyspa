from django.db import models
from django.contrib.auth.models import AbstractUser


class TaiKhoan(AbstractUser):
    username = None  # Không dùng username mặc định, dùng ten_dang_nhap
    ten_dang_nhap = models.CharField(max_length=50, unique=True)
    mat_khau = models.CharField(max_length=128)  # Django sẽ hash tự động
    email = models.EmailField(unique=True)
    so_dien_thoai = models.CharField(max_length=15, blank=True, null=True)
    ngay_tao = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'ten_dang_nhap'  # Đăng nhập bằng ten_dang_nhap
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.ten_dang_nhap


class KhachHang(models.Model):
    id_taikhoan = models.OneToOneField(TaiKhoan, on_delete=models.CASCADE, primary_key=True)
    ho_ten = models.CharField(max_length=100)
    dia_chi = models.CharField(max_length=255, blank=True)
    ngay_sinh = models.DateField(blank=True, null=True)
    gioi_tinh = models.CharField(max_length=1, choices=[('M', 'Nam'), ('F', 'Nữ')], blank=True)
    ngay_tham_gia = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ho_ten


class NhanVien(models.Model):
    id_taikhoan = models.OneToOneField(TaiKhoan, on_delete=models.CASCADE, primary_key=True)
    ho_ten = models.CharField(max_length=100)
    chuc_vu = models.CharField(max_length=50)
    ngay_vao_lam = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ho_ten


class QuanTriVien(models.Model):
    id_taikhoan = models.OneToOneField(TaiKhoan, on_delete=models.CASCADE, primary_key=True)
    ho_ten = models.CharField(max_length=100)
    quyen_han = models.CharField(max_length=50, default='full')
    ngay_tao_quyen = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ho_ten


# Các models khác từ ERD (thêm dần nếu cần)
class ThuCung(models.Model):
    id_khachhang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    ten_thucung = models.CharField(max_length=100)
    loai = models.CharField(max_length=50)
    tuoi = models.IntegerField()
    ghi_chu = models.TextField(blank=True)


# ... (thêm các models còn lại tương tự: DichVu, LichHen, v.v.)
from django.db import models

# Create your models here.
