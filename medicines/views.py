
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import Medicine
from .forms import MedicineForm


# ══════════════════════════════════
#  AUTH VIEWS
# ══════════════════════════════════

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Karibu, {user.username}! 👋')
            return redirect('dashboard')
        else:
            messages.error(request, '❌ Jina au nywila si sahihi.')
    else:
        form = AuthenticationForm()

    return render(request, 'medicines/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Umetoka mfumoni.')
    return redirect('login')


# ══════════════════════════════════
#  DASHBOARD
# ══════════════════════════════════

@login_required
def dashboard_view(request):
    today     = timezone.now().date()
    soon_date = today + timedelta(days=30)

    total_medicines  = Medicine.objects.count()
    expired_count    = Medicine.objects.filter(expiry_date__lt=today).count()
    expiring_count   = Medicine.objects.filter(
                           expiry_date__gte=today,
                           expiry_date__lte=soon_date
                       ).count()
    good_count       = Medicine.objects.filter(expiry_date__gt=soon_date).count()

    # Dawa 5 za hivi karibuni kuongezwa
    recent_medicines = Medicine.objects.order_by('-date_added')[:5]

    context = {
        'total_medicines' : total_medicines,
        'expired_count'   : expired_count,
        'expiring_count'  : expiring_count,
        'good_count'      : good_count,
        'recent_medicines': recent_medicines,
    }
    return render(request, 'medicines/dashboard.html', context)


# ══════════════════════════════════
#  MEDICINE VIEWS
# ══════════════════════════════════

@login_required
def medicine_list(request):
    query     = request.GET.get('search', '')
    medicines = Medicine.objects.all()

    if query:
        medicines = medicines.filter(name__icontains=query)

    return render(request, 'medicines/medicine_list.html', {
        'medicines': medicines,
        'query'    : query,
    })


@login_required
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Dawa imeongezwa!')
            return redirect('medicine_list')
        else:
            messages.error(request, '❌ Hitilafu! Angalia tena.')
    else:
        form = MedicineForm()

    return render(request, 'medicines/add_medicine.html', {'form': form})


@login_required
def edit_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Dawa imesasishwa!')
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)

    return render(request, 'medicines/add_medicine.html', {
        'form'   : form,
        'editing': True,
        'medicine': medicine,
    })


@login_required
def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    medicine.delete()
    messages.success(request, '🗑️ Dawa imefutwa.')
    return redirect('medicine_list')


@login_required
def expired_medicines(request):
    today     = timezone.now().date()
    medicines = Medicine.objects.filter(expiry_date__lt=today)
    return render(request, 'medicines/expired.html', {'medicines': medicines})


@login_required
def expiring_soon(request):
    today     = timezone.now().date()
    soon_date = today + timedelta(days=30)
    medicines = Medicine.objects.filter(
        expiry_date__gte=today,
        expiry_date__lte=soon_date
    )
    return render(request, 'medicines/expiring_soon.html', {'medicines': medicines})
# Create your views here.
